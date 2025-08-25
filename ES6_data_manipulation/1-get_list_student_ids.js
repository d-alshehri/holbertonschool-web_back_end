export default function getListStudentIds(input) {
    if (!Array.isArray(input)) {
        return [];
    }
    else{
        return input.map(student => student.id)
    }
}
