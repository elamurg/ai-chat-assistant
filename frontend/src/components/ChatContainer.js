// chat interface

import React, { useState, useEffect, useRef } from "react";
import styled from "styled-components";
import { Send, Bot, User, Loader } from 'lucide-react';
import { chatAPI } from '/frontend/src/services/api';

const Container = styled.div`
   width: 100%;
   max-width: 800px;
   height: 600px;
   background: white;
   border-radius: 1rem;
   box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
   display: flex;
   flex-direction: column;
   overflow: hidden;
`;

const Header = styled.div`
   background: ${props => props.theme.colors.primary};
   color: white;
   padding; 1.5rem;
   text-align: center;
`;

const ChatContainer = () => {
    const [messages, setMessages] = useState([
        {
            role: 'assistant',
            content: 'Hello! I am your AI assistant. What would you like to learn today?',
        },
    ]);
    const [inputMessage, setInputMessage] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    const handleSendMessage = async () => {
        if (!inputMessage.trim()) return;

        const userMessage = {
            role: 'user',
            content: inputMessage.trim(),
        };
        setMessages(prev => [...prev, userMessage]);
        setInputMessage('')
        setIsLoading(true);

        try {
            const response = await chatAPI.sendMessage(userMessage.content, messages);
            if (response.success) {
                setMessages(prev => [...prev, {
                    role: 'assistant',
                    content: response.response,
                }]);
            }
        } catch (err) {
          console.error('Chat error:', err);
        } finally {
          setIsLoading(false);
        }
    };
    return (
        <Container>
            <Header>
                <h1>AI Chat Assistant</h1>
                <p>Powered by Gemini</p>
            </Header>
        </Container>
    );
};

export default ChatContainer;