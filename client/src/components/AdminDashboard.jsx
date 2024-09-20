import React, { useState, useEffect } from 'react';
import axios from 'axios';

const AdminDashboard = () => {
  const [users, setUsers] = useState([]);
  const [billingInfo, setBillingInfo] = useState([]);

  useEffect(() => {
    fetchUsers();
    fetchBillingInfo();
  }, []);

  const fetchUsers = async () => {
    try {
      const response = await axios.get('/api/admin/users');
      setUsers(response.data);
    } catch (error) {
      console.error('Error fetching users:', error);
    }
  };

  const fetchBillingInfo = async () => {
    try {
      const response = await axios.get('/api/admin/billing');
      setBillingInfo(response.data);
    } catch (error) {
      console.error('Error fetching billing info:', error);
    }
  };

  return (
    <div className="admin-dashboard">
      <h1>Admin Dashboard</h1>
      <section>
        <h2>Users</h2>
        <ul>
          {users.map(user => (
            <li key={user.id}>{user.email} - {user.role}</li>
          ))}
        </ul>
      </section>
      <section>
        <h2>Billing Information</h2>
        <ul>
          {billingInfo.map(info => (
            <li key={info.id}>{info.user} - ${info.amount}</li>
          ))}
        </ul>
      </section>
    </div>
  );
};

export default AdminDashboard;