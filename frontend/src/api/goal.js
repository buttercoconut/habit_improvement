import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000',
});

export const fetchGoals = async (userId) => {
  const response = await api.get(`/goals/`, { params: { user_id: userId } });
  return response.data;
};

export const createGoal = async (goal) => {
  const response = await api.post('/goals/', goal);
  return response.data;
};
