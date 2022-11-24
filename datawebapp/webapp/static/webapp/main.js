$(".summary-data-table-toggler").hide();

$(document).ready(function () {

$('#sidebarCollapse').on('click', function () {
    $('#sidebar, #content').toggleClass('active');
    $(this).toggleClass('active');
});

$('#summaryDataTable').DataTable({});
$('#summaryDataTableHead').DataTable({
                                        searching:false,
                                        paging:false
                                        });
$('.dataTables_length').addClass('bs-select');

$(".show-full-data-table").click(function(){
    $(".summary-data-table-toggler").toggle();
});
});