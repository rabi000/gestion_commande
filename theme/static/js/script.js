
$(document).ready(function () {
    
    window.setTimeout(function () {
        $('.msg').fadeTo(500, 0).slideToggle(500, function () {
            $(this).remove()
        });
       
        
    }, 1500);
    
    
    $("  #div_id_ligne_cinq, #div_id_ligne_cinq_qte, #div_id_ligne_cinq_prix_unitaire, #div_id_ligne_cinq_prix_total, #div_id_ligne_six, #div_id_ligne_six_qte, #div_id_ligne_six_prix_unitaire, #div_id_ligne_six_prix_total, #div_id_ligne_sept, #div_id_ligne_sept_qte, #div_id_ligne_sept_prix_unitaire, #div_id_ligne_sept_prix_total,  #div_id_ligne_huit, #div_id_ligne_huit_qte, #div_id_ligne_huit_prix_unitaire,#div_id_ligne_huit_prix_total").hide()
    
    $(".plus_ligne").click(function () {
        
        $("#div_id_ligne_cinq, #div_id_ligne_cinq_qte, #div_id_ligne_cinq_prix_unitaire, #div_id_ligne_cinq_prix_total").slideToggle(200)
        $("#div_id_ligne_six, #div_id_ligne_six_qte, #div_id_ligne_six_prix_unitaire, #div_id_ligne_six_prix_total").slideToggle(200)
        $("#div_id_ligne_sept, #div_id_ligne_sept_qte, #div_id_ligne_sept_prix_unitaire, #div_id_ligne_sept_prix_total").slideToggle(200)
        $("#div_id_ligne_huit, #div_id_ligne_huit_qte, #div_id_ligne_huit_prix_unitaire, #div_id_ligne_huit_prix_total").slideToggle(200)
    })
    
    
    $("#id_ligne_un_qte, #id_ligne_un_prix_unitaire,#id_ligne_deux_qte, #id_ligne_deux_prix_unitaire, #id_ligne_trois_qte, #id_ligne_trois_prix_unitaire, #id_ligne_quatre_qte, #id_ligne_quatre_prix_unitaire, #id_ligne_cinq_qte, #id_ligne_cinq_prix_unitaire, #id_ligne_six_qte, #id_ligne_six_prix_unitaire, #id_ligne_sept_qte, #id_ligne_sept_prix_unitaire, #id_ligne_huit_qte, #id_ligne_huit_prix_unitaire").keyup(function () {
        var ligne_un_qte_text = $('#id_ligne_un_qte').val();
        var ligne_un_prix_unitaire_text = $('#id_ligne_un_prix_unitaire').val();
        var ligne_un_total = ligne_un_qte_text * ligne_un_prix_unitaire_text
            
        var ligne_deux_qte_text = $('#id_ligne_deux_qte').val();
        var ligne_deux_prix_unitaire_text = $('#id_ligne_deux_prix_unitaire').val();
        var ligne_deux_total = ligne_deux_qte_text * ligne_deux_prix_unitaire_text
            
        var ligne_trois_qte_text = $('#id_ligne_trois_qte').val();
        var ligne_trois_prix_unitaire_text = $('#id_ligne_trois_prix_unitaire').val();
        var ligne_trois_total = ligne_trois_qte_text * ligne_trois_prix_unitaire_text
            
        var ligne_quatre_qte_text = $('#id_ligne_quatre_qte').val();
        var ligne_quatre_prix_unitaire_text = $('#id_ligne_quatre_prix_unitaire').val();
        var ligne_quatre_total = ligne_quatre_qte_text * ligne_quatre_prix_unitaire_text
            

        var ligne_cinq_qte_text = $('#id_ligne_cinq_qte').val();
        var ligne_cinq_prix_unitaire_text = $('#id_ligne_cinq_prix_unitaire').val();
        var ligne_cinq_total = ligne_cinq_qte_text * ligne_cinq_prix_unitaire_text

        var ligne_six_qte_text = $('#id_ligne_six_qte').val();
        var ligne_six_prix_unitaire_text = $('#id_ligne_six_prix_unitaire').val();
        var ligne_six_total = ligne_six_qte_text * ligne_six_prix_unitaire_text

        var ligne_sept_qte_text = $('#id_ligne_sept_qte').val();
        var ligne_sept_prix_unitaire_text = $('#id_ligne_sept_prix_unitaire').val();
        var ligne_sept_total = ligne_sept_qte_text * ligne_sept_prix_unitaire_text

        var ligne_huit_qte_text = $('#id_ligne_huit_qte').val();
        var ligne_huit_prix_unitaire_text = $('#id_ligne_huit_prix_unitaire').val();
        var ligne_huit_total = ligne_huit_qte_text * ligne_huit_prix_unitaire_text

        var total = ligne_un_total + ligne_deux_total + ligne_trois_total + ligne_quatre_total + ligne_cinq_total + ligne_six_total + ligne_sept_total + ligne_huit_total;
            
        $("#id_ligne_un_prix_total").val(ligne_un_total);
        $("#id_ligne_deux_prix_total").val(ligne_deux_total);   
        $("#id_ligne_trois_prix_total").val(ligne_trois_total); 
        $("#id_ligne_quatre_prix_total").val(ligne_quatre_total);
        $("#id_ligne_cinq_prix_total").val(ligne_cinq_total);
        $("#id_ligne_six_prix_total").val(ligne_six_total);
        $("#id_ligne_sept_prix_total").val(ligne_sept_total);
        $("#id_ligne_huit_prix_total").val(ligne_huit_total);
        $("#id_total").val(total);

    })

    $('#table').paging({ limit:7 });
    
});


var verify_data_table = $("#chk_data_table").length;
if (verify_data_table == 0) {
    $("#no_data").text("Aucune donnée a été trouver");
    }
 