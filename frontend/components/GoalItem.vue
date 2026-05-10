<template>
  <li class="goal-item" :class="{ completed: goal.completed }">
    <div class="goal-details">
      <h3>{{ goal.title }}</h3>
      <p>{{ goal.description }}</p>
    </div>
    <div class="goal-actions">
      <button @click="toggleComplete(goal.id)" title="Toggle complete">
        {{ goal.completed ? 'Undo' : 'Complete' }}
      </button>
      <button @click="deleteGoal(goal.id)" title="Delete goal">Delete</button>
    </div>
  </li>
</template>

<script setup>
import { defineEmits } from 'vue';

const props = defineProps({
  goal: {
    type: Object,
    required: true,
  },
});

const emit = defineEmits(['toggleComplete', 'deleteGoal']);

function toggleComplete(id) {
  emit('toggleComplete', id);
}

function deleteGoal(id) {
  emit('deleteGoal', id);
}
</script>

<style scoped>
.goal-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem;
  border-bottom: 1px solid #ddd;
}
.goal-item.completed h3,
.goal-item.completed p {
  text-decoration: line-through;
  color: #888;
}
.goal-actions button {
  margin-left: 0.5rem;
}
</style>
