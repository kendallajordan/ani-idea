import { useState } from "react";

export default function TitleInputForm({ setTitles }) {
  const [inputFields, setInputFields] = useState([""]);

  // Updates an input field if changed
  const handleInputChange = (index, event) => {
    const values = [...inputFields];
    values[index] = event.target.value;
    setInputFields(values);
  };

  // Adds a new input field (max 5) to the form
  const handleAddField = () => {
    if (inputFields.length < 5) {
      setInputFields([...inputFields, ""]);
    }
  };

  // Submits the list of anime titles
  const handleSubmit = (event) => {
    event.preventDefault();

    // Only keep non-empty input fields
    setTitles(inputFields.filter((title) => title.trim() !== ""));
  };

  return (
    <form onSubmit={handleSubmit}>
      {inputFields.map((input, index) => (
        <input
          key={index}
          type="text"
          value={input}
          onChange={(event) => handleInputChange(index, event)}
          placeholder={`Enter Anime Title #${index + 1}`}
        />
      ))}
      <button
        type="button"
        onClick={handleAddField}
        disabled={inputFields.length >= 5}
      >
        Add Another Title
      </button>
      <button type="submit">Get Recommendations</button>
    </form>
  );
}
