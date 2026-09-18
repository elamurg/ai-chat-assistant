// Building the API service
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api',
  timeout: 30000,
  headers: {
    'Content-type': 'application/json',
  },
});

export const chatAPI = {
    sendMessage: async (MessageChannel, conversationHistory = []) => {
        try {
            const response = await apiClient.post('/chat', {
                message,
                conversationHistory: conversationHistory,
            });
            return response.data;
        } catch (error) {
            throw new Error(error.response?.data?.detail || 'Failed to send message');
        }
    },
};