import config from '../env/config';

export function login(email, password, remember) {
  const formData = new URLSearchParams();
  formData.set('email', email);
  formData.set('password', password);
  formData.set('remember', remember);

  return fetch(`${config.api}/user/login`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: formData,
    credentials: 'include',
  });
}

export function register(email, password) {
  const formData = new URLSearchParams();
  formData.set('email', email);
  formData.set('password', password);

  return fetch(`${config.api}/user/signup`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: formData,
    credentials: 'include',
  });
}

export function logout() {
  return fetch(`${config.api}/user/logout`, {
    method: 'POST',
    credentials: 'include',
  });
}

export function profile() {
  return fetch(`${config.api}/user/profile`, {
    credentials: 'include',
  });
}

export function resetPassword(oldPassword, newPassword) {
  const formData = new URLSearchParams();
  formData.set('oldpassword', oldPassword);
  formData.set('password', newPassword);

  return fetch(`${config.api}/user/changepassword`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: formData,
    credentials: 'include',
  });
}
