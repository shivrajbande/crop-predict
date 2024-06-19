const express = require('express');
const multer = require('multer');
const path = require('path');

const app = express();
const upload = multer();

// Set up EJS as the templating engine
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Middleware to parse URL-encoded data
app.use(express.urlencoded({ extended: true }));

// Define your crop dictionary
const crop_dict = {
    1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
    8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
    14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
    19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
};

app.get('/', (req, res) => {
    res.render('index', { result: null });
});

app.post('/predict', upload.none(), (req, res) => {
    const { Nitrogen, Phosporus, Potassium, Temperature, Humidity, Ph, Rainfall } = req.body;

    // Example prediction logic based on provided features
    let predicted_crop_label;

    // Replace with your actual prediction logic
    if (parseFloat(Nitrogen) > 80 && parseFloat(Phosporus) < 40) {
        predicted_crop_label = 2; // Example prediction label for Maize
    } else if (parseFloat(Temperature) > 20.5 && parseFloat(Rainfall) < 200) {
        predicted_crop_label = 1; // Example prediction label for Rice
    } else if (parseFloat(Potassium) > 65 && parseFloat(Humidity) > 78) {
        predicted_crop_label = 6; // Example prediction label for Papaya
    } else if (parseFloat(Ph) < 6.5 && parseFloat(Nitrogen) < 85) {
        predicted_crop_label = 3; // Example prediction label for Jute
    } else {
        predicted_crop_label = 0; // Example label for unknown crop
    }

    // Map predicted crop label to crop name using crop_dict
    const predicted_crop_name = crop_dict[predicted_crop_label] || "Unknown";

    // Prepare result message based on prediction
    let result;
    if (predicted_crop_name !== "Unknown") {
        result = `${predicted_crop_name} is the best crop to be cultivated right there.`;
    } else {
        result = "Sorry, we could not determine the best crop to be cultivated with the provided data.";
    }

    // Render the result in the view
    res.render('index', { result });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
