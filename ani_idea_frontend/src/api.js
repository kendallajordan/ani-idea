import axios from 'axios';

const API_URL = 'http://localhost:8000/api/recommend/';

export const getRecommendations = async (titles) => {
  try {
    const response = await axios.post(API_URL, { titles });
    console.log(response);
    return response.data;
  } catch (error) {
    console.error('Error fetching recommendations:', error);
    throw error; // Re-throw the error so it can be caught in App.jsx
  }
};
