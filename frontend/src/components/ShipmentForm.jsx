// ShipmentForm.jsx
import React, { useState } from "react";
import axios from "axios";

const ShipmentForm = () => {
  const [origin, setOrigin] = useState({ lat: "", lng: "" });
  const [destination, setDestination] = useState({ lat: "", lng: "" });
  const [weight, setWeight] = useState(0);
  const [carrierId, setCarrierId] = useState(1);
  const [description, setDescription] = useState("");
  const [response, setResponse] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post("/shipments/", {
        origin: { latitude: parseFloat(origin.lat), longitude: parseFloat(origin.lng) },
        destination: { latitude: parseFloat(destination.lat), longitude: parseFloat(destination.lng) },
        weight_kg: weight,
        carrier_id: carrierId,
        description,
      });
      setResponse(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div>
      <h2>Create Shipment</h2>
      <form onSubmit={handleSubmit}>
        <label>Origin Latitude: <input value={origin.lat} onChange={(e) => setOrigin({ ...origin, lat: e.target.value })} /></label>
        <label>Origin Longitude: <input value={origin.lng} onChange={(e) => setOrigin({ ...origin, lng: e.target.value })} /></label>
        <label>Destination Latitude: <input value={destination.lat} onChange={(e) => setDestination({ ...destination, lat: e.target.value })} /></label>
        <label>Destination Longitude: <input value={destination.lng} onChange={(e) => setDestination({ ...destination, lng: e.target.value })} /></label>
        <label>Weight (kg): <input type="number" value={weight} onChange={(e) => setWeight(parseFloat(e.target.value))} /></label>
        <label>Carrier ID: <input type="number" value={carrierId} onChange={(e) => setCarrierId(parseInt(e.target.value))} /></label>
        <label>Description: <input value={description} onChange={(e) => setDescription(e.target.value)} /></label>
        <button type="submit">Create</button>
      </form>
      {response && <pre>{JSON.stringify(response, null, 2)}</pre>}
    </div>
  );
};

export default ShipmentForm;
