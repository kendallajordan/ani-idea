import styles from "./RecommendationList.module.css";
import AnimeCard from "./AnimeCard";

export default function RecommendationList({ recommendations }) {
  return (
    <div className={styles.listContainer}>
      {recommendations.map((anime, index) => (
        <AnimeCard key={index} anime={anime} />
      ))}
    </div>
  );
}
