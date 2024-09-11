const express = require('express');
const http = require('http');
const socketIo = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

// Middleware to serve static files
app.use(express.static('public'));

// Socket.io connection
io.on('connection', (socket) => {
    console.log('New client connected');
    
    // Example: Notification when a document is uploaded
    socket.on('document_uploaded', (data) => {
        io.emit('new_notification', { message: 'New document uploaded!', data });
    });

    socket.on('disconnect', () => {
        console.log('Client disconnected');
    });
});

const PORT = process.env.PORT || 5000;
server.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
