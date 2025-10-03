$(document).ready(function(){
    $("#toggleBtn").on("click", function(){
        $("#historia").toggleClass("expandido");
        if($(this).text() === "Ler mais"){
            $(this).text("Ler menos");
        } else {
            $(this).text("Ler mais");
        }
    });
});