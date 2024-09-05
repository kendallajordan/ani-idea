// Basic right now, later turn this into a list component with "list item components"
// index is index, anime is the anime object, use dot notation to reference a field from the object
export default function RecommendationList({ recommendations }) {
  return (
    <div>
      <h2>Recommended Anime:</h2>
      <ul>
        {recommendations.map((anime, index) => (
          <li key={index}>
            {anime["Name"]}
          </li>
        ))}
      </ul>
    </div>
  );
}
