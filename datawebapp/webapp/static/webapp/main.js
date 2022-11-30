$(".summary-data-table-toggler").hide();

// initialize tooltips
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})
//

$(document).ready(function () {

$('#sidebarCollapse').on('click', function () {
    $('#sidebar, #content').toggleClass('active');
    $(this).toggleClass('active');
});

$('#summaryDataTable').DataTable({
                                  scrollY: '200px',
                                  scrollCollapse: true,
                                  fixedHeader: true
                                });
$('#summaryDataTableHead').DataTable({
                                        searching:false,
                                        paging:false
                                        });
$('.dataTables_length').addClass('bs-select');

$(".show-full-data-table").click(function(){
    $(".summary-data-table-toggler").toggle();
});
});