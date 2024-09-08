import styles from "./AnimeCard.module.css";

export default function AnimeCard({ anime }) {
  return (
    <div className={styles.card}>
      <img
        className={styles.image}
        src={anime["Image URL"]}
        alt={anime["Name"]}
      />
      <div className={styles.cardContent}>
        <h3 className={styles.title}>{anime["Name"]}</h3>
        {anime['English name'] !== 'UNKNOWN' && (
          <p className={styles.englishTitle}>
            {`(${anime["English name"]})`}
          </p>
        )}
        <p className={styles.source}>Source: {anime["Source"]}</p>
        <p className={styles.synopsis}>{anime["Synopsis"]}</p>
        <p className={styles.genres}>Genres: {anime["Genres"]}</p>
      </div>
    </div>
  );
}
