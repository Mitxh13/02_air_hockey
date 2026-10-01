"""
collisions: puck-vs-paddle collision handling.
"""


def handle_paddle_collision(puck, paddle):
    """
    If the puck overlaps the paddle, reflect its velocity along the
    collision normal (the line connecting the paddle centre to the puck
    centre) and push the puck out so it never gets stuck inside.
    Returns True if a collision was handled this frame.
    """
    dx = puck.x - paddle.x
    dy = puck.y - paddle.y
    distance = (dx ** 2 + dy ** 2) ** 0.5

    min_dist = puck.radius + paddle.radius

    if distance < min_dist:
        # Avoid division by zero when centres overlap exactly
        if distance == 0:
            dx, dy, distance = 1.0, 0.0, 1.0

        # Unit normal pointing from paddle centre toward puck centre
        nx = dx / distance
        ny = dy / distance

        # Reflect velocity: v' = v - 2(v·n)n
        dot = puck.vx * nx + puck.vy * ny
        puck.vx -= 2 * dot * nx
        puck.vy -= 2 * dot * ny

        # Push puck just outside the paddle so it can't collide again
        overlap = min_dist - distance
        puck.x += nx * overlap
        puck.y += ny * overlap

        return True

    return False
