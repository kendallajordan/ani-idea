import styles from "./Header.module.css";
import myAnimeImage from "../assets/anime_header.jpg";

export default function Header() {
  return (
    <header
      className={styles.header}
      style={{ backgroundImage: `url(${myAnimeImage})` }}
    ></header>
  );
}
