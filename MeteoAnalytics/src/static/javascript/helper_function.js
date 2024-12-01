function prepareData(data) {
    // Controlla se i dati sono un array
    if (!Array.isArray(data)) {
        console.error("I dati forniti non sono un array:", data);
        return [];
    }

    let heatData = [];

    data.forEach(row => {
        let timestamp = row["Data_Ora"];
        let benzene = parseFloat(row["Benzene (µg/m³)"]);

        // Salta righe con dati non validi
        if (!timestamp || isNaN(benzene)) return;

        // Latitudine e longitudine
        let latitude = parseFloat(row["Latitudine"]); 
        let longitude = parseFloat(row["Longitudine"]);

        // Aggiungi al dataset per la heatmap
        heatData.push([latitude, longitude, benzene]);
    });

    return heatData;
}
