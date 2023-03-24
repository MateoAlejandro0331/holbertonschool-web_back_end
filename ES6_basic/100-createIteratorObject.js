export default function createIteratorObject(report) {
  const employeesList = [];
  for (const employee of Object.values(report.allEmployees)) {
    employeesList.push(...employee);
  }
  return employeesList;
}
