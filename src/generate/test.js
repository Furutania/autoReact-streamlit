import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import HomePage from './HomePage';
import ArticlePage from './ArticlePage';
import './App.css';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/article">
          <ArticlePage />
        </Route>
        <Route path="/">
          <HomePage />
        </Route>
      </Switch>
    </Router>
  );
}

export default App;
/*END_FILE: src/App.js*/