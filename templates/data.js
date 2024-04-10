// Sample temperature data for 12 hours
const temperatureData = {{ temp_data['daily_list'] }};
const ctx = document.getElementById('temperatureChart').getContext('2d');
const temperatureChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '11:00', '10:00', '12:00'],
        datasets: [{
            label: 'Temperature (°C)',
            data: temperatureData,
            fill: true,
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1,
            
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

// Sample temperature data for different time frames
const dailyData = {{ temp_data['daily_list'] }}; // ... up to 24 values
const weeklyData =  {{ temp_data['weekly_list'] }}; // one value for each day of the week
const monthlyData =  {{ temp_data['monthly_list'] }}; // ... up to 30 or 31 values

const dayHours = ['00:00','01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00']; // ... up to 24 labels
const weekDays = ['الاحد', 'الاثنين', 'الثلاثاء', 'الاربعاء', 'الخميس', 'الجمعة','السبت'];
const monthDays = Array.from({ length: 30 }, (_, i) => (i + 1).toString()); // Generate labels from 1 to 30

// Function to update the chart
function updateChart(chart, data, labels) {
chart.data.labels = labels;
chart.data.datasets.forEach((dataset) => {
dataset.data = data;
});
chart.update();
}

// Event listeners for buttons
document.getElementById('dayBtn').addEventListener('click', function() {
updateChart(temperatureChart, dailyData, dayHours);
});
document.getElementById('weekBtn').addEventListener('click', function() {
updateChart(temperatureChart, weeklyData, weekDays);
});
document.getElementById('monthBtn').addEventListener('click', function() {
updateChart(temperatureChart, monthlyData, monthDays);
});

