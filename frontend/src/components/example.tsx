import React, { useState, useEffect } from "react";

const ExampleComponent: React.FC = () => {
  const [data, setData] = useState<any>(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/users/")
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then((result) => setData(result))
      .catch((error) => console.error("Error fetching data:", error));
  }, []);

  return (
    <div>
      <h2>Example Component</h2>
      {data ? (
        <div>
          <p>Data from Django:</p>
          <ul>
            {data.map((item: any) => (
              <li key={item.id}>
                {item.first_name} {item.last_name} - {item.email}
              </li>
            ))}
          </ul>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default ExampleComponent;
