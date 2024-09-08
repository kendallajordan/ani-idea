import styles from './Description.module.css';

export default function Description() {
  return (
    <div className={styles.descriptionContainer}>
      <p className={styles.descriptionText}>
        Welcome to Ani-Idea, the Anime Recommendation System. <br />
        Please tell us your favorite anime, and we will find you some recommendations! <br />
        <strong style={{ color: "#df0000" }}>** This build currently supports anime series released up to the year 2023 **</strong>
      </p>
    </div>
  );
}