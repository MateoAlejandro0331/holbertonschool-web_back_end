export default function createReportObject(employeesList) {
  return {
    allEmployees: employeesList,
    getNumberOfDepartments(department) {
      return Object.keys(department).length;
    },
  };
}
