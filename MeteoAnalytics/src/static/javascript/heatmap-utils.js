// Inizializza la heatmap e aggiungila alla mappa
function initializeHeatmap(map) {
    return L.heatLayer([], {
        radius: 25,
        blur: 15,
        maxZoom: 17
    }).addTo(map);
}

// Aggiorna i dati della heatmap
function updateHeatmap(heatmapLayer, data) {
    heatmapLayer.setLatLngs(data);
}

// Avvia l'animazione
function startAnimation(hourlyData, heatmapLayer) {
    let timestamps = Object.keys(hourlyData);
    let currentIndex = 0;

    setInterval(() => {
        const currentTimestamp = timestamps[currentIndex];
        const dataForCurrentTime = hourlyData[currentTimestamp];

        updateHeatmap(heatmapLayer, dataForCurrentTime);

        document.getElementById("time-label").innerText = `Ora: ${currentTimestamp}`;
        currentIndex = (currentIndex + 1) % timestamps.length;
    }, 1000);
}

// Esponi le funzioni al contesto globale
window.initializeHeatmap = initializeHeatmap;
window.updateHeatmap = updateHeatmap;
window.startAnimation = startAnimation;
