export default function hasValuesFromArray(set, array){
    return array.every(x => set.has(x))
}