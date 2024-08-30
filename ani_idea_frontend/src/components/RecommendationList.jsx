// Basic right now, later turn this into a list component with "list item components"
export default function RecommendationList({ recommendations }) {
  return (
    <div>
      <h2>Recommended Anime:</h2>
      <ul>
        {recommendations.map((anime, index) => (
          <li key={index}>
            {anime}
          </li>
        ))}
      </ul>
    </div>
  );
}
