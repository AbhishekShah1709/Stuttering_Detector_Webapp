import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css'

import Recorder from './components/record_play.component.js'
import UploadFileSystem from './components/upload-file.component.js'
function App() {
    return (
        <Router>
            <div className="container">
            <nav className="navbar navbar-expand-lg">
            <Link to="/" className="navbar-brand">App</Link>
            <div className="collapse navbar-collapse">
            <ul className="navbar-nav mr-auto">
            <li className="navbar-item">
            <Link to="/record" className="nav-link">Record</Link>
            </li>
            <li className="navbar-item">
            <Link to="/upload" className="nav-link">Upload File</Link>
            </li>
            </ul>
            </div>
            </nav>

    <Route path="/record" exact component={Recorder}/>
    <Route path="/upload" exact component={UploadFileSystem}/>

    </div>
    </Router>
  );
}

export default App;
