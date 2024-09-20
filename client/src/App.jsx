import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import PrivateRoute from './components/PrivateRoute';
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import AdminDashboard from './components/AdminDashboard';

const App = () => {
  return (
    <Router>
      <Switch>
        <Route exact path="/login" component={Login} />
        <PrivateRoute exact path="/" component={Dashboard} />
        <PrivateRoute exact path="/admin" component={AdminDashboard} isAdmin={true} />
      </Switch>
    </Router>
  );
};

export default App;