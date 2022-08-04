const deleteStudentEnrollment = async (studentEnrollmentId) => {
  const formData = new FormData();
  formData.append('student_enrollment_id', studentEnrollmentId);

  const response = await fetch(`/student_enrollments/${studentEnrollmentId}`, {
      method: 'DELETE',
      body: formData
  });
  const res = await response.json();

  $(".modal").modal('toggle');
  // Citation for removing a row dynamically
  // Date: 08/01/2022
  // Adapted from 
  // Source URL: https://stackoverflow.com/questions/21756777/jquery-find-element-by-data-attribute-value 
  $(`#browse tr[data-student-enrollment-id="${studentEnrollmentId}"]`).remove();
}


const wireTableDeleteButtons = () => {
  // Citation for opening and closing the modal
  // Date: 08/01/2022
  // Copied from 
  // Source URL: https://stackoverflow.com/questions/33650266/bootstrap-modal-open-button-requires-two-clicks-to-reopen-after-closing 
  $("#browse").on("click", ".btn-modal-delete", function() {
    $(".modal").modal('toggle');
    $(".modal").data('student-enrollment-id', $(this).data('student-enrollment-id'));
    $(".modal-title").text('Delete Student Enrollment');
    $(".modal-body").text(`Are you sure you want to delete Student Enrollment ID ${$(this).data('student-enrollment-id')}?`);
    $(".modal-footer .btn-primary").addClass('btn-delete');
    $(".modal-footer .btn-primary").text('Delete');
    $(".btn-delete").prop('disabled', false);
  });
}


const wireDeleteButton = () => {
  $(".modal").on("click", '.btn-delete', function() {
    let studentEnrollmentId = $(".modal").data('student-enrollment-id')
    $(this).prop('disabled', true);
    deleteStudentEnrollment(studentEnrollmentId);
  });
}

const wireTableUpdateButtons = () => {
  $("#browse").on("click", ".btn-update", function() {
    let studentEnrollmentId = $(this).data('student-enrollment-id')
    window.location.replace(`/student_enrollments/${studentEnrollmentId}`);
  });
}


$(document).ready(function() {
  wireTableDeleteButtons();
  wireDeleteButton();
  wireTableUpdateButtons();
})