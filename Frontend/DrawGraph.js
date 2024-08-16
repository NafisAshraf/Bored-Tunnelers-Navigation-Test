import React, { useEffect, useState } from "react";
import Plot from "react-plotly.js";
import io from "socket.io-client";

const DrawGraph = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        const newSocket = io('http://localhost:5000');

        newSocket.on('connect', () => {
            console.log('Connected to server');
        });

        newSocket.on('disconnect', () => {
            console.log('Disconnected from server');
        });

        newSocket.on('new_number', (msg) => {
            setData((currentData) => [...currentData, { x: msg.x, y: msg.y, z: msg.z }]);
        });

        return () => newSocket.disconnect();
    }, []);

    useEffect(() => {
        console.log(data);
    }, [data]);

    return (
        <div>
            <Plot
                data={[
                    {
                        x: data.map(point => point.x),
                        y: data.map(point => point.y),
                        z: data.map(point => point.z),
                        type: 'scatter3d',
                        mode: 'markers',
                        marker: { color: 'red' },
                    },
                ]}
                layout={{ width: 800, height: 400, title: 'Real-time 3D Data' }}
            />
        </div>
    );
}

export default DrawGraph;