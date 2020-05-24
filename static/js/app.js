const canvas = d3.select(".canva");
const svg = canvas.append("svg").attr('width',800).attr('height',800);

getInputValue();
async function getInputValue(){
            // Selecting the input element and get its value
            const values = document.getElementById("myInput").value;

console.log(values)
const xlabels = [];
const yvalues = [];
chartIt();

async function chartIt(){
        await getData();
        const ctx = document.getElementById('myChart').getContext('2d');
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: xlabels,
                datasets: [{
                    label: '# of Votes',
                    data: yvalues,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)'

                    ],
                    options: {
                        layout: {
                            padding: {
                                left: 50,
                                right: 0,
                                top: 0,
                                bottom: 0
                            }
                        }
                    },
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });
      }


    getData();
    async function getData(){

        const response = await fetch("test.csv");
        const data = await response.text();

        const table = data.split('\n').slice(1);
        table.forEach(row=>{
            const columns = row.split(',');
            const YearStarted = columns[0]
            xlabels.push(YearStarted);
            const RegistrationStart = columns[1]
            const RegistrationEnd = columns[2]
            const PlanCode = columns[3]
            const PlanDescription = columns[4]
            const Majors = columns[5]
            const StudentNumber = columns[6]
            const Streamline = columns[7]
            const ProbOfMatheStreamline = columns[8]
            const ProbOfPhysicsStreamline= columns[9]
            const ProbofEarthStreamline = columns[10]
            const ProbofBioStreamline = columns[11]
            const ProbofUnknownStreamline = columns[12]
            const FirstYearSubjects = columns[13]
            const AggregateYOS1 = columns[14]

            const ProgressoutcomeYOS1 = columns[15]
            const Firstyearoutcome= columns[16]
            const SecondYearSubjects= columns[17]
            const AggregateYOS2 = columns[18]
            const ProgressoutcomeYOS2 = columns[19]
            const Secondyearoutcome = columns[20]
            const ThirdYearSubjects = columns[21]
            const AggregateYOS3= columns[22]
            const ProgressoutcomeYOS3 = columns[23]
            const Finaloutcome = columns[24]
            const UnknownYearSubjects= columns[25]
            const Aggregate = columns[26]
            const Qualified = columns[27]

            if(values == "abc" ){
                yvalues.push(AggregateYOS1)
                }

        });
    }
    }