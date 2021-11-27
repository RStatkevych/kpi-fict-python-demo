const BASE_URL = 'http://0.0.0.0'


async function register(userData) {
  const url = `${BASE_URL}/auth/register`;
  const response = await fetch(url, {
    method: 'POST',
    mode: 'cors',
    cache: 'no-cache',
    credentials: 'same-origin',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(userData),
    referrerPolicy: 'same-origin'
  });
  return await response.json();
}

async function getCurrentUserProfile(token) {
  const url = `${BASE_URL}/profile/me`;
  const r = await fetch(url, {
    method: 'GET',
    cache: 'no-cache',
    mode: 'cors',
    credentials: 'same-origin',
    headers: {
      'Token': token,
      'Content-Type': 'application/json',
    },
    referrerPolicy: 'same-origin'
  })
  const data = await r.json();
  if (!r.ok) {
    throw data.error
  }
  return data
}

async function login(userData) {
  const url = `${BASE_URL}/auth/login`;
  const r = await fetch(url, {
    method: 'POST',
    cache: 'no-cache',
    mode: 'cors',
    credentials: 'same-origin',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(userData),
    referrerPolicy: 'same-origin'
  })
  const data = await r.json();
  if (!r.ok) {
    throw data.error
  }
  return data
}
async function getUsersByName(token, name) {
  const url = `${BASE_URL}/users?name=${name}`;
  const r = await fetch(url, {
    method: 'GET',
    cache: 'no-cache',
    mode: 'cors',
    credentials: 'same-origin',
    headers: {
      'Token': token,
      'Content-Type': 'application/json',
    },
    params: {
      'name': name
    },
    referrerPolicy: 'same-origin'
  })
  const data = await r.json();
  if (!r.ok) {
    throw data.error
  }
  return data.users
}

async function getUserProfile(token, id) {

    const url = `${BASE_URL}/profile/${id}`
    const r = await fetch(url, {
      method: 'GET',
      cache: 'no-cache',
      mode: 'cors',
      credentials: 'same-origin',
      headers: {
        'Token': token,
        'Content-Type': 'application/json',
      },
      referrerPolicy: 'same-origin'
    })
    const data = await r.json();
    if (!r.ok) {
      throw data.error
    }
    return data
}


export  {
  register,
  login,
  getCurrentUserProfile,
  getUsersByName,
  getUserProfile
};
