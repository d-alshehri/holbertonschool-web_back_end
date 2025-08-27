return Promise.allSettled([userPromise, photoPromise])
  .then(results =>
    results.map(result => {
      if (result.status === 'fulfilled') {
        return { status: result.status, value: result.value };
      } else {
        return { status: result.status, value: result.reason.toString() };
      }
    })
  );
