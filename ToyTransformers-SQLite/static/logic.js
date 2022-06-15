d3.json("/toytable").then(data => {
    console.log(data);
    buildTable(data);
});
function buildTable(data){
    var table=document.getElementById('myTable')

    for (var i=0 ;i <data.length;i++){
        var row=`<tr> 
                    <td>${data[i].Product}</td>
                    <td>${data[i].Supplier}</td>
                    <td>${data[i].Price}</td>
                    <td>${data[i].Unit}</td>
                    <td>${data[i].Location}</td>
                </tr>`
        table.innerHTML+=row
        
    }
}