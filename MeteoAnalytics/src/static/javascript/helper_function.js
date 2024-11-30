function prepareData(data) {
    // Controlla se i dati sono un array
    if (!Array.isArray(data)) {
        console.error("I dati forniti non sono un array:", data);
        return {};
    }

    let hourlyData = {};

    data.forEach(row => {
        let timestamp = row["Data_Ora"];
        let benzene = parseFloat(row["Benzene (µg/m³)"]);

        // Salta righe con dati non validi
        if (!timestamp || isNaN(benzene)) return;

        // Latitudine e longitudine fittizi per la demo
        let latitude = parseFloat(row["Data_Ora"]); 
        let longitude = parseFloat(row["Data_Ora"]);

        // Crea una nuova chiave per ogni ora
        if (!hourlyData[timestamp]) hourlyData[timestamp] = [];
        hourlyData[timestamp].push([latitude, longitude, benzene]);
    });

    return hourlyData;
}
