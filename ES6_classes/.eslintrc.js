module.exports = {
  env: {
    browser: true,
    es6: true,
  },
  extends: [
    'airbnb-base',
  ],
  rules: {
      'no-underscore-dangle': ['error', { allow: ['_maxStudentsSize'] }],
  },
};
