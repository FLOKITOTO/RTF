import { lazy, useState, useCallback, useEffect, Suspense } from "react";
import {
  Redirect,
  Route,
  useLocation,
  Switch,
  HashRouter as Router,
} from "react-router-dom";
import "./App.css";

import Header from "./components/Header";
import Menu from "./components/Menu";
import ButtonMenu from "./components/ButtonMenu";

const ChangeTitle = ({ title }) => {
  const titleName = title.replace(/-/g, " ");
  useEffect(() => {
    document.title = titleName;
  }, [titleName]);

  return <h2 className="title">{titleName}</h2>;
};

const Child = ({ id, text }) => {
  const location = useLocation();
  const LoadComponent = lazy(() =>
    import(
      /* webpackChunkName: "[request]" */ `./pages${location.pathname}.js`
    ).catch(() => import("./components/NotFound.js"))
  );

  return (
    <>
      <ChangeTitle title={location.pathname.replace(/\//, " ")} />
      <LoadComponent />
    </>
  );
};

function App() {
  const [info, setInfo] = useState("");
  const [id, setID] = useState("");
  const [text, setText] = useState("");
  const callback = useCallback((id, text, info) => {
    setInfo(info);
    setID(id);
    setText(text);
  }, []);

  return (
    <Router>
      <div className="grid">
        <Menu parentCallback={callback} />
        <Header />
        <main id="section-example">
          <Suspense fallback={<div>Page is Loading...</div>}>
            <Switch>
              <Route exact path="/">
                <Redirect to="/home" />
              </Route>
              <Route
                path="/:id"
                children={<Child id={id} info={info} text={text} />}
              />
            </Switch>
          </Suspense>
        </main>
      </div>
      <ButtonMenu />
    </Router>
  );
}

export default App;
