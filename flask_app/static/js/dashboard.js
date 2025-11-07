// Dashboard Analytics JavaScript
// Fetches and displays analytics data using Chart.js

document.addEventListener('DOMContentLoaded', function() {
    loadAnalytics();
});

async function loadAnalytics() {
    try {
        const response = await fetch('/api/analytics');
        const data = await response.json();

        if (data.total_responses === 0) {
            document.getElementById('noDataMessage').style.display = 'block';
            document.getElementById('summaryStats').style.display = 'none';
            document.querySelectorAll('.charts-grid').forEach(el => el.style.display = 'none');
            return;
        }

        // Update summary stats
        updateSummaryStats(data);

        // Create charts
        createRiskDistributionChart(data.risk_distribution, data.total_responses);
        createPHQ2DistributionChart(data.phq2_distribution);
        createRiskFactorsChart(data.risk_factors, data.total_responses);
        createCareSettingsChart(data.care_settings);

    } catch (error) {
        console.error('Error loading analytics:', error);
        alert('Failed to load analytics data.');
    }
}

function updateSummaryStats(data) {
    document.getElementById('totalResponses').textContent = data.total_responses;
    document.getElementById('highRiskCount').textContent = data.risk_distribution.HIGH_RISK || 0;
    document.getElementById('lowRiskCount').textContent = data.risk_distribution.LOW_RISK || 0;

    const highRiskPercent = data.total_responses > 0
        ? ((data.risk_distribution.HIGH_RISK || 0) / data.total_responses * 100).toFixed(1)
        : 0;
    document.getElementById('highRiskPercent').textContent = highRiskPercent + '%';
}

function createRiskDistributionChart(riskDist, total) {
    const ctx = document.getElementById('riskDistributionChart').getContext('2d');

    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['High Risk', 'Low Risk'],
            datasets: [{
                data: [
                    riskDist.HIGH_RISK || 0,
                    riskDist.LOW_RISK || 0
                ],
                backgroundColor: ['#EF4444', '#10B981'],
                borderWidth: 2,
                borderColor: '#fff'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        padding: 20,
                        font: {
                            size: 14,
                            family: 'Inter'
                        }
                    }
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const label = context.label || '';
                            const value = context.parsed || 0;
                            const percent = ((value / total) * 100).toFixed(1);
                            return `${label}: ${value} (${percent}%)`;
                        }
                    }
                }
            }
        }
    });
}

function createPHQ2DistributionChart(phq2Dist) {
    const ctx = document.getElementById('phq2DistributionChart').getContext('2d');

    // Prepare data for scores 0-6
    const scores = [0, 1, 2, 3, 4, 5, 6];
    const counts = scores.map(score => phq2Dist[score] || 0);

    // Color bars: red for >=3 (clinical cutoff), blue for <3
    const backgroundColors = scores.map(score =>
        score >= 3 ? '#EF4444' : '#4F46E5'
    );

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: scores.map(s => s.toString()),
            datasets: [{
                label: 'Number of Respondents',
                data: counts,
                backgroundColor: backgroundColors,
                borderRadius: 8
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        title: function(context) {
                            const score = context[0].label;
                            return `PHQ-2 Score: ${score}`;
                        },
                        label: function(context) {
                            return `Count: ${context.parsed.y}`;
                        }
                    }
                }
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'PHQ-2 Score (Clinical Cutoff: ≥3)',
                        font: {
                            size: 14,
                            family: 'Inter'
                        }
                    },
                    grid: {
                        display: false
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Count',
                        font: {
                            size: 14,
                            family: 'Inter'
                        }
                    },
                    beginAtZero: true,
                    ticks: {
                        precision: 0
                    }
                }
            }
        }
    });
}

function createRiskFactorsChart(riskFactors, total) {
    const ctx = document.getElementById('riskFactorsChart').getContext('2d');

    const labels = [
        'Prior MH Treatment',
        'Meds for Mood/Anxiety',
        'Fair/Poor Health',
        'No Regular Exercise',
        'Dieting',
        'Overweight/Obese'
    ];

    const data = [
        riskFactors.prior_mh || 0,
        riskFactors.mh_meds || 0,
        riskFactors.poor_health || 0,
        riskFactors.no_exercise || 0,
        riskFactors.dieting || 0,
        riskFactors.overweight || 0
    ];

    // Calculate percentages
    const percentages = data.map(count => (count / total * 100).toFixed(1));

    // Color: major risk factors (first 3) in red, lifestyle factors in orange
    const backgroundColors = [
        '#EF4444', '#EF4444', '#EF4444',
        '#F59E0B', '#F59E0B', '#F59E0B'
    ];

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Prevalence',
                data: percentages,
                backgroundColor: backgroundColors,
                borderRadius: 8
            }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const index = context.dataIndex;
                            const count = data[index];
                            const percent = context.parsed.x;
                            return `${count} respondents (${percent}%)`;
                        }
                    }
                }
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Percentage of Respondents',
                        font: {
                            size: 14,
                            family: 'Inter'
                        }
                    },
                    beginAtZero: true,
                    max: 100,
                    ticks: {
                        callback: function(value) {
                            return value + '%';
                        }
                    }
                },
                y: {
                    grid: {
                        display: false
                    }
                }
            }
        }
    });
}

function createCareSettingsChart(careSettings) {
    const ctx = document.getElementById('careSettingsChart').getContext('2d');

    const labels = Object.keys(careSettings);
    const data = Object.values(careSettings);

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Number of Respondents',
                data: data,
                backgroundColor: '#4F46E5',
                borderRadius: 8
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return `Count: ${context.parsed.y}`;
                        }
                    }
                }
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Typical Care Setting',
                        font: {
                            size: 14,
                            family: 'Inter'
                        }
                    },
                    grid: {
                        display: false
                    },
                    ticks: {
                        maxRotation: 45,
                        minRotation: 45
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Count',
                        font: {
                            size: 14,
                            family: 'Inter'
                        }
                    },
                    beginAtZero: true,
                    ticks: {
                        precision: 0
                    }
                }
            }
        }
    });
}
