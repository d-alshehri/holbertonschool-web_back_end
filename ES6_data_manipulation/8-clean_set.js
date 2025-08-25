export default function cleanSet(set, startString) {
    if ( typeof startString !== 'string' || !startString) return ''; // handle missing startString
  
    return Array.from(set)
      .filter(value => value.startsWith(startString))
      .map(value => value.slice(startString.length))
      .join('-');
  }
  