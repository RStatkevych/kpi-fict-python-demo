import {useParams} from 'react-router-dom';
import {useEffect,useState,useContext} from 'react';
import {getUserProfile} from './Client';
import {Context} from './Context';
import { InputGroup, FormControl, Button, Card,
  Col, Row, Container, Alert, ListGroup, Form} from 'react-bootstrap';
import ProfileInfo from './ProfileInfo'


export default function SpecificProfile() {
  const {id} = useParams();
  const [{token}, dispatch] = useContext(Context);
  const [userData, setUserData] = useState({});
  const [error, setError] = useState('');
  useEffect(() => {
    getUserProfile(token, id).then(setUserData).catch(setError);
  },[]);
  return (error === '' ?
    <ProfileInfo userData={userData} /> :
    <Alert variant="danger">
    {error}
    </Alert>
  );
}
