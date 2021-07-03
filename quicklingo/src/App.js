
import { BrowserRouter as Router,Route, Switch } from "react-router-dom";
import Main from "./lingoPages/Main"
import Chinese from "./lingoPages/Chinese"


function App(){
  return(
    <Router>
      <Switch>
        <Route exact path="/" component={Main} />
        <Route exact path="/chinese" component={Chinese} />
      </Switch>
    </Router>
  );
}
export default App;