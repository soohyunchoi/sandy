import './App.css';
import React, { Component } from 'react';
import { BrowserRouter } from 'react-router-dom'
import { Route, Link } from 'react-router-dom'
import SurfSpotsList from './SurfSpotsList'
import SurfSpotCreateUpdate from './SurfSpotCreateUpdate'
import './App.css';
const  BaseLayout  = () => (
  <div  className="container-fluid">
      <nav  className="navbar navbar-expand-lg navbar-light bg-light">
          <a  className="navbar-brand"  href="#">Sandy</a>
          <button  className="navbar-toggler"  type="button"  data-toggle="collapse"  data-target="#navbarNavAltMarkup"  aria-controls="navbarNavAltMarkup"  aria-expanded="false"  aria-label="Toggle navigation">
          <span  className="navbar-toggler-icon"></span>
      </button>
      <div  className="collapse navbar-collapse"  id="navbarNavAltMarkup">
          <div  className="navbar-nav">
              <a  className="nav-item nav-link"  href="/">SURFSPOTS</a>
              <a  className="nav-item nav-link"  href="/surfspot">CREATE SURFSPOT</a>
          </div>
      </div>
      </nav>
      <div  className="content">
          <Route  path="/"  exact  component={SurfSpotsList}  />
          <Route  path="/surfspot/:pk"  component={SurfSpotCreateUpdate}  />
          <Route  path="/surfspot/"  exact  component={SurfSpotCreateUpdate}  />
      </div>
  </div>
  )
class App extends Component {
  render() {
    return (<BrowserRouter>
      <BaseLayout/>
    </BrowserRouter>);
  }
}

export default App;
