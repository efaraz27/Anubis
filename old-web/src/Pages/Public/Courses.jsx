import React, {useState} from 'react';
import {useSnackbar} from 'notistack';
import axios from 'axios';

import Grid from '@material-ui/core/Grid';
import Grow from '@material-ui/core/Grow';
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import TextField from '@material-ui/core/TextField';
import makeStyles from '@material-ui/core/styles/makeStyles';

import StandardLayout from '../../Components/Layouts/StandardLayout';
import CourseCard from '../../Components/Public/Courses/CourseCard';
import standardErrorHandler from '../../Utils/standardErrorHandler';
import standardStatusHandler from '../../Utils/standardStatusHandler';


const useStyles = makeStyles((theme) => ({
  inline: {
    display: 'inline',
  },
}));


const joinCourse = (state, enqueueSnackbar) => () => {
  const {joinCode, setReset} = state;
  axios.get(`/api/public/courses/join/${encodeURIComponent(joinCode)}`).then((response) => {
    const data = standardStatusHandler(response, enqueueSnackbar);
    if (data) {
      if (data.status.match(/Joined/)) {
        setReset((prev) => ++prev);
      }
    }
  }).catch(standardErrorHandler(enqueueSnackbar));
};


export default function CourseView() {
  const classes = useStyles();
  const {enqueueSnackbar} = useSnackbar();
  const [courses, setCourses] = useState([]);
  const [joinCode, setJoinCode] = useState(null);
  const [joinOpen, setJoinOpen] = useState(false);
  const [reset, setReset] = useState(0);

  React.useEffect(() => {
    axios.get('/api/public/courses/').then((response) => {
      const data = standardStatusHandler(response, enqueueSnackbar);
      if (data) {
        setCourses(data.courses);
      }
    }).catch(standardErrorHandler(enqueueSnackbar));
  }, [reset]);

  const state = {
    courses, setCourses,
    joinCode, setJoinCode,
    joinOpen, setJoinOpen,
    reset, setReset,
  };

  return (
    <StandardLayout title={'Anubis'} description={'Courses'}>
      <Dialog
        open={joinOpen}
        onClose={() => setJoinOpen(false)}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <DialogTitle id="alert-dialog-title">Join an Anubis Class</DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
            Provide your join code here to join your class!
          </DialogContentText>
          <TextField
            placeholder={'Join Code'}
            variant={'outlined'}
            style={{width: '100%'}}
            value={joinCode}
            onChange={(e) => setJoinCode(e.target.value)}
          />
        </DialogContent>
        <DialogActions>
          <Button
            color="primary"
            variant={'contained'}
            onClick={joinCourse(state, enqueueSnackbar)}
            autoFocus
          >
            Join
          </Button>
        </DialogActions>
      </Dialog>
      <Grid container spacing={4}>
        <Grid item xs={12}>
          <Button color={'primary'} variant={'contained'} onClick={() => setJoinOpen(true)}>
            Join Class
          </Button>
        </Grid>
        {courses.map((course, pos) => (
          <Grid item xs={12} md={6} lg={3} key={course.courseCode}>
            <Grow
              in={true}
              style={{transformOrigin: '0 0 0'}}
              timeout={300 * (pos + 1)}
            >
              <CourseCard course={course}/>
            </Grow>
          </Grid>
        ))}
      </Grid>
    </StandardLayout>
  );
}
