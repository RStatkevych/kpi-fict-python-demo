import {Context} from './Context'
import {useContext, useEffect, useState} from 'react'
import {getCurrentUserProfile, getUsersByName} from './Client'
import { InputGroup, FormControl, Button, Card,
  Col, Row, Container, Alert, ListGroup, Form} from 'react-bootstrap';
import {useNavigate} from 'react-router-dom';
import ProfileInfo from './ProfileInfo'

export default function Profile() {
  const [{token}, dispatch] = useContext(Context)
  const [userProfile, setUserProfile] = useState({})
  const [users, setUsers] = useState([])
  const navigate = useNavigate()
  useEffect(() => getCurrentUserProfile(token).then(setUserProfile),[])

  const onChange = (event) => {
    getUsersByName(token, event.target.value).then(setUsers);
  }
  return token === null ?
      <Alert variant="danger">
        Not authorised
      </Alert> :
      <>
        <ProfileInfo userData={userProfile} />


        <Card style={{marginTop: '10px'}}>
          <Card.Header>Search Users</Card.Header>
          <Card.Body>
            <Form.Control type="text" placeholder="Normal text" onChange={onChange} />
            <ListGroup>
            {
              users.map((v, i) => {
                return <ListGroup.Item action key={i}
                    onClick={() => navigate(`/profile/${v.id}`)}
                  >{v.name}</ListGroup.Item>
              })
            }
            </ListGroup>
          </Card.Body>
        </Card>
      </>

}
