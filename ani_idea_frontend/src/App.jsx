import './App.css';
import { useEffect, useState } from "react";
import TitleInputForm from "./components/TitleInputForm";
import RecommendationList from "./components/RecommendationList";
import { getRecommendations } from "./api";
import Header from "./components/Header";
import ProjectTitle from "./components/ProjectTitle";
import Description from './components/Description';

function App() {
  const [titles, setTitles] = useState([]);
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchRecommendations = async () => {
      if (titles.length > 0) {
        setLoading(true);
        setError(null);

        try {
          const response = await getRecommendations(titles);
          setRecommendations(response);
        } catch (error) {
          console.error("Error fetching recommendations: ", error);
          setError(
            "Sorry, couldn't get your recommendations. Please try again!"
          );
        }
        setLoading(false);
      }
    };

    fetchRecommendations();
  }, [titles]);

  return (
    <div>
      <Header />
      <ProjectTitle />
      <Description />
      <TitleInputForm setTitles={setTitles} />
      {error && <p style={{ color: "red" }}>{error}</p>}
      {loading ? (
        <p>Loading recommendations...</p>
      ) : (
        <RecommendationList recommendations={recommendations} />
      )}
    </div>
  );
}

export default App;
