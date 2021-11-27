import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link
} from "react-router-dom";
import Login from './Login'
import Register from './Register'
import Profile from './Profile'
import Home from './Home'
import SpecificProfile from './SpecificProfile'
import Layout from './Layout'
import 'bootstrap/dist/css/bootstrap.min.css';
import Store from './Context'

export default function App() {
  return (<>
    <Store>
      <Router>
          {/* A <Switch> looks through its children <Route>s and
              renders the first one that matches the current URL. */}
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route path='/profile/*' element={<Layout>
              <Routes>
                <Route path=":id" element={<SpecificProfile />} />
                <Route path="" element={<Profile />} />
              </Routes>
            </Layout>} />
          </Routes>
      </Router>

    </Store>
    </>
  );
}
