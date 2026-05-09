// validator.js
const fs = require("fs");
const path = require("path");

const requiredFiles = [
  "backend/app/main.py",
  "backend/app/config.py",
  "backend/app/models/shipment.py",
  "backend/app/services/shipment_service.py",
  "backend/app/api/shipments.py",
  "frontend/src/components/ShipmentForm.jsx",
  "frontend/src/App.jsx",
  "frontend/src/index.js",
];

requiredFiles.forEach((file) => {
  const fullPath = path.join(__dirname, file);
  if (!fs.existsSync(fullPath)) {
    console.error(`Missing required file: ${file}`);
    process.exit(1);
  }
});

console.log("All required files exist.");
