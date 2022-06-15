d3.json("/toy").then(data => {
    console.log(data);
    d3.select("#test").text(data)
    
});